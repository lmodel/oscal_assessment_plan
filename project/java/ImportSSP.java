package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Used by the assessment plan and POA&M to import information about the system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImportSSP  {

  private String href;
  private String remarks;

}