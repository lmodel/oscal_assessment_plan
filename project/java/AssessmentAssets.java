package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Identifies the assets used to perform this assessment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentAssets  {

  private List<SystemComponent> components;
  private List<AssessmentPlatform> assessment-platforms;

}