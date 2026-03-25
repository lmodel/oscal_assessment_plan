package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Used to define various terms and conditions under which an assessment can be performed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TermsAndConditions  {

  private List<AssessmentPart> parts;

}